from django.core.paginator import Paginator
from firstapp.models import *
from user.models import *
from django.shortcuts import *
from user.views.common_views import *
import random
import re


def showColorStone(request, product_id):
    product = get_object_or_404(
        Inventoryofcolorstones, pk=product_id, frontend=True)
    if not product:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    all_colorstone_id_list = Inventoryofcolorstones.objects.filter(frontend=True).exclude(id=product.id).values_list('id',
                                                                                                                     flat=True)
    random_colorstone_id_list = random.sample(
        list(all_colorstone_id_list), min(len(all_colorstone_id_list), 10))
    related_products = Inventoryofcolorstones.objects.filter(
        id__in=random_colorstone_id_list)

    user = None
    if 'user_email' in request.session.keys():
        user = User_table.objects.get(pk=request.session['user_email'])

    # regex to extract youtube id from iframe src
    try:
        pattern = r'<iframe .* src="[^"]*/([^"]+)"'
        search = re.search(pattern, product.media.video_embed_link)
        youtube_video_id = search[1]
    except:
        youtube_video_id = None

    return render(request, 'colorstone_templates/colorstone_product_page.html', {'product': product, 'user': user, 'related_products': related_products, 'youtube_video_id': youtube_video_id})
