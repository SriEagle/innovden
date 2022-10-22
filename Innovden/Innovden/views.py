from django.shortcuts import redirect, render
from app.models import Categories, Course, Level, ReviewRating, Video, UserCourse
from django.template.loader import render_to_string
from django.http import JsonResponse
from app.forms import ReviewForm
from django.contrib import messages
from django.db.models import Sum



def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('id')

    context = {
        'category': category,
        'course': course,
    }
    return render(request, 'Main/home.html', context)


def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price=0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()

    context = {
        'category': category,
        'level': level,
        'course': course,
        'FreeCourse_count': FreeCourse_count,
        'PaidCourse_count': PaidCourse_count,
    }
    return render(request, 'Main/single_course.html', context)


def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
        course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in=category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course': course
    }

    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category
    }
    return render(request, 'Main/contact_us.html', context)


def ABOUT_US(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category
    }
    return render(request, 'Main/about_us.html', context)


def SEARCH_COURSE(request):
    category = Categories.get_all_category(Categories)

    query = request.GET['query']
    course = Course.objects.filter(title__icontains=query)

    context = {
        'course': course,
        'category': category
    }

    return render(request, 'search/search.html', context)


def COURSE_DETAILS(request, slug, ):


    category = Categories.get_all_category(Categories)
    starone = ReviewRating.objects.filter(course__slug=slug, rating__gte=0, rating__lte=20).count()
    startwo = ReviewRating.objects.filter(course__slug=slug, rating__gte=21, rating__lte=40).count()
    starthree = ReviewRating.objects.filter(course__slug=slug, rating__gte=41, rating__lte=60).count()
    starfour = ReviewRating.objects.filter(course__slug=slug, rating__gte=61, rating__lte=80).count()
    starfive = ReviewRating.objects.filter(course__slug=slug, rating__gte=81, rating__lte=100).count()

    reviews = ReviewRating.objects.filter(course__slug=slug, status='True')
    total_rating = ReviewRating.objects.filter(course__slug=slug).aggregate(sum=Sum('rating'))
    time_duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    number_rating = ReviewRating.objects.filter(course__slug=slug).count()

    course_id = Course.objects.get(slug=slug)

    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None


    course = Course.objects.filter(slug=slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course': course,
        'category': category,
        'reviews': reviews,
        'total_rating': total_rating,
        'time_duration': time_duration,
        'number_rating': number_rating,
        'starone': starone,
        'startwo': startwo,
        'starthree': starthree,
        'starfour': starfour,
        'starfive': starfive,
        'check_enroll': check_enroll,


    }

    return render(request, 'course/course_details.html', context)


def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }

    return render(request, 'error/404.html', context)


def submit_review(request, course_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, course__id=course_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()

            messages.success(request, 'Thank you! Your Review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.course_id = course_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your Review has been updated.')
                return redirect(url)


def CHECKOUT(request, slug):
    course = Course.objects.get(slug=slug)

    if course.price == 0:
        course = UserCourse(
            user=request.user,
            course=course,
        )
        course.save()
        return redirect('home')

    return render(request, 'checkout/checkout.html')


def MY_COURSE(request):
    return render(request, 'course/my_course.html')
