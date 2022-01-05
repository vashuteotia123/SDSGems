from firstapp.models import *


def diamond_common_context(request):
    user_login = False
    if 'is_logedin' in request.session:
        user_login = True
    diamond_shapes = shape_d.objects.all()[:4]
    diamond_cuts = clarity.objects.all()[:4]
    diamond_origins = color_origin.objects.all()[:4]
    diamond_polishes = polish.objects.all()[:4]
    return {
        'diamond_shapes': diamond_shapes,
        'diamond_cuts': diamond_cuts,
        'diamond_origins': diamond_origins,
        'diamond_polishes': diamond_polishes,
        'user_login' : user_login,
        'only_cs': True,
    }

def jewellery_common_context(request):
    return {
    'jewellery_types' : jewell.objects.all()[:4],
    'jewellery_centerstones' : centerstone.objects.all()[:4],
    'jewellery_shapes' : shape1.objects.all()[:4],
    'jewellery_metals' : metal1.objects.all()[:4],
    }

def colorstone_common_context(request):
    return {
    'colorstone_origins' : Origin_cs.objects.all()[:4],
    'colorstone_gemtypes' : gemtype.objects.all()[:4],
    'colorstone_shapes' : shape_cs.objects.all()[:4],
    'colorstone_colors' : color_of_colorstone.objects.all()[:4],
    } 