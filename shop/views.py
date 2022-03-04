from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@api_view(['GET'])
def req_email(request):
    data = {
        "name": request.data['name'],
        "email": request.data['email'],
        "time": datetime.datetime.now()
    }
    html = render_to_string("email_templates.html", data)
    text_string = strip_tags(html)
    email = EmailMultiAlternatives(
        "Test Email",
        text_string,
        settings.EMAIL_HOST_USER,
        [data['email']]
    )
    email.attach_alternative(html, "text/html")
    email.send()
    return Response({"msg": "Email sent to " + str(data['email'])})


@api_view(['GET'])
def api_home(request):
    data = {
        "base_url": "http://127.0.0.1:8000/api"
    }
    return render(request, "api_home.html", context=data)


@api_view(['GET'])
def home(request):
    return render(request, "home.html", )


# GET CATEGORY

@api_view(['GET'])
def get_category(request):
    category = Categories.objects.all()
    cs = CategoriesSerializers(category, many=True)
    return Response({"status": 200, "data": cs.data})


@api_view(['GET'])
def get_category_one(request, cat_id):
    category = Categories.objects.get(cat_id=cat_id)
    cs = CategoriesSerializers(category, many=False)
    return Response({"status": 200, "data": cs.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_category(request):
    cs = CategoriesSerializers(data=request.data)
    if not cs.is_valid():
        return Response({"status": 401, "data": cs.errors})
    cs.save()
    return Response({"status": 201, "data": cs.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_category(request, cat_id):
    cat = Categories.objects.get(cat_id=cat_id)
    serializer = CategoriesSerializers(instance=cat, data=request.data)
    if not serializer.is_valid():
        return Response({"status": 401, "data": serializer.errors})
    serializer.save()
    return Response({"status": 200, "data": serializer.data})


# GET TAG
@api_view(['GET'])
def get_tag(request):
    tag = Tags.objects.all()
    cs = TagsSerializers(tag, many=True)
    return Response({"status": 200, "data": cs.data})


@api_view(['GET'])
def get_tag_one(request, tag_id):
    tag = Tags.objects.get(tag_id=tag_id)
    cs = TagsSerializers(tag, many=False)
    return Response({"status": 200, "data": cs.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_tag(request):
    ts = TagsSerializers(data=request.data)
    if not ts.is_valid():
        return Response({"status": 401, "data": ts.errors})
    ts.save()
    return Response({"status": 200, "data": ts.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_tag(request, tag_id):
    tag = Tags.objects.get(tag_id=tag_id)
    serializer = TagsSerializers(instance=tag, data=request.data)
    if not serializer.is_valid():
        return Response({"status": 401, "data": serializer.errors})
    serializer.save()
    return Response({"status": 200, "data": serializer.data})


# PRODUCT
@api_view(['GET'])
def get_products(request, tag_title=None, cat_title=None):
    prd = None
    if cat_title is not None:
        prd = Products.objects.filter(cats__cat_title=cat_title)

    if tag_title is not None:
        prd = Products.objects.filter(tags__tag_title=tag_title)

    if prd is None:
        prd = Products.objects.all()
    ps = ProductsSerializers(prd, many=True)
    return Response({"status": 200, "data": ps.data})


@api_view(['GET'])
def get_single_product(request, p_id):
    products = Products.objects.get(p_id=p_id)
    ps = ProductsSerializers(products, many=False)
    return Response({"status": 200, "data": ps.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_products(request):
    ps = ProductsSerializers(data=request.data)
    if not ps.is_valid():
        return Response({"status": 401, "massage": ps.errors})
    ps.save()
    return Response({"status": 200, "data": ps.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_products(request, p_id):
    products = Products.objects.get(p_id=p_id)
    ps = ProductsSerializers(instance=products, data=request.data)
    if not ps.is_valid():
        return Response({"status": 401, "massage": ps.errors})
    ps.save()
    return Response({"status": 201, "data": ps.data})


@api_view(['GET'])
def get_orders(request):
    orders = Orders.objects.all()
    ors = OrdersSerializers(orders, many=True)
    return Response({"status": 200, "data": ors.data})


@api_view(['GET'])
def get_single_orders(request, customer_id=None, order_id=None):
    if customer_id is None and order_id is not None:
        orders = Orders.objects.filter(order_id=order_id)
    if customer_id is not None and order_id is None:
        orders = Orders.objects.filter(customer__customer_id=customer_id)
    if customer_id is not None and order_id is not None:
        orders = Orders.objects.filter(customer__customer_id=customer_id, order_id=order_id)
    serializers = OrdersSerializers(orders, many=True)
    return Response({"status": 200, "data": serializers.data})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_orders(request):
    ors = OrdersSerializers(data=request.data)
    if not ors.is_valid():
        return Response({"status": 401, "massage": ors.errors})
    ors.save()
    return Response({"status": 201, "data": ors.data})


@api_view(['POST'])
def register(request):
    username = request.data['username']
    customer = {}
    user = UsersSerializer(data=request.data)
    if user.is_valid():
        user.save()
        customer['customer_name'] = request.data['customer_name']
        customer['user_id'] = (User.objects.last()).id
        custSer = CustomerSerializers(data=customer)
        users = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=users)
        print(token)
        print(created)
        if custSer.is_valid():
            custSer.save()
            return Response({"status": 201, "data": custSer.data, "token": str(token)})
        else:
            return Response({"status": 201, "data": custSer.errors})
    else:
        return Response({"status": 401, "data": user.errors})


@api_view(['POST'])
def login(request):
    user = User.objects.get(username=request.data['username'])
    userSerializer = UsersSerializer(user, many=False)
    if userSerializer is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": 201, "data": userSerializer.data, "token": str(token)})
    else:
        return Response({"status": 201, "data": "Invalid Username & Password Combination"})
