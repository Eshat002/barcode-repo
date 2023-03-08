from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
# Create your views here.
from .models import Write


def index(request):
    print(request.POST)
    context = {}
    if request.method == "POST":
        Write.objects.create(name=request.POST.get('qr_text'))
        # factory = qrcode.image.svg.SvgImage
        # img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        # stream = BytesIO()
        # img.save(stream)
        # context["svg"] = stream.getvalue().decode()
        context['img']=Write.objects.all().last().qr_code.url
        # print(Write.objects.all().last())

    return render(request, "index.html", context=context)