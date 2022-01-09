from django.core.paginator import Paginator
from firstapp.models import *
from user.models import *
from django.shortcuts import *
from user.views.common_views import *
import random
import re


@myuser_login_required
def showDiamond(request, product_id):
    product = get_object_or_404(
        Inventoryofdiamond, pk=product_id, frontend=True)
    if not product:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    all_diamond_id_list = Inventoryofdiamond.objects.filter(
        frontend=True).exclude(id=product.id).values_list('id',  flat=True)
    random_diamond_id_list = random.sample(
        list(all_diamond_id_list), min(len(all_diamond_id_list), 10))
    related_products = Inventoryofdiamond.objects.filter(
        id__in=random_diamond_id_list)

    # regex to extract youtube id from iframe src
    try:
        pattern = r'<iframe .* src="[^"]*/([^"]+)"'
        search = re.search(pattern, product.media.video_embed_link)
        youtube_video_id = search[1]
    except:
        youtube_video_id = None

    return render(request, 'diamond_templates/diamond_product_page.html', {'product': product, 'user': User_table.objects.get(pk=request.session['user_email']), 'related_products': related_products, 'youtube_video_id': youtube_video_id})