from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET'])
def home(request):
    return Response({"PAGE": "API HOME"})


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
def set_category(request):
    cs = CategoriesSerializers(data=request.data)
    if not cs.is_valid():
        return Response({"status": 401, "data": cs.errors})
    cs.save()
    return Response({"status": 201, "data": cs.data})


@api_view(['POST'])
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
    cs = CategoriesSerializers(tag, many=True)
    return Response({"status": 200, "data": cs.data})


@api_view(['GET'])
def get_tag_one(request, tag_id):
    tag = Categories.objects.get(tag_id=tag_id)
    cs = CategoriesSerializers(tag, many=False)
    return Response({"status": 200, "data": cs.data})


@api_view(['POST'])
def set_tag(request):
    ts = TagsSerializers(data=request.data)
    if not ts.is_valid():
        return Response({"status": 401, "data": ts.errors})
    ts.save()
    return Response({"status": 200, "data": ts.data})


@api_view(['POST'])
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

    # if cat_title is not None:
    #     cat = Categories.objects.get(cat_title=cat_title)
    #     print(cat)
    # if tag_title is not None:
    #     tag = Tags.objects.get(tag_title=tag_title)
    #     prd = tag.orders_set.all()
    #
    # if prd is None:
    #     prd = Products.objects.select_related().all()
    #     ps = ProductsSerializers(prd, many=True)
    #     return Response({"status": 200, "data": ps.data})
    # else:
    #     return Response({"status": 404, "data": "Not Found"})


@api_view(['GET'])
def get_single_product(request, p_id):
    products = Products.objects.get(p_id=p_id)
    ps = ProductsSerializers(products, many=False)
    return Response({"status": 200, "data": ps.data})


@api_view(['POST'])
def set_products(request):
    ps = ProductsSerializers(data=request.data)
    if not ps.is_valid():
        return Response({"status": 401, "massage": ps.errors})
    ps.save()
    return Response({"status": 200, "data": ps.data})


@api_view(['POST'])
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
        orders = Orders.objects.filter(customers_customer_id=customer_id)
    if customer_id is not None and order_id is not None:
        orders = Orders.objects.filter(customers_customer_id=customer_id, orders_order_id=order_id)
    serializers = OrdersSerializers(orders, many=True)
    return Response({"status": 200, "data": serializers.data})


@api_view(['POST'])
def get_orders(request):
    ors = OrdersSerializers(data=request.data)
    if not ors.is_valid():
        return Response({"status": 401, "massage": ors.errors})
    return Response({"status": 201, "data": ors.data})


@api_view(['GET'])
def get_orders(request, params):
    orders = Orders.objects.select_related()
    ors = OrdersSerializers(orders, many=True)
    return Response({"status": 200, "data": ors.data})
