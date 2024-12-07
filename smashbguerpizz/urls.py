"""
URL configuration for smashbguerpizz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import base64
import io
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
import numpy as np

import matplotlib.pyplot as plt

def home(request):
    bytes_array = []
    sizes_name_edge = np.array([['SMALL', 'MEDIUM', 'LARGE', 'XLARGE'], [4, 8, 10, 12], [27, 30, 35, 40]])
    fig_size_a = 2
    fig_size_b = 2
    sizes = [[1,1,1,1], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1]]
 
    for i in range(4):
        
        fig, ax = plt.subplots(figsize=(fig_size_a, fig_size_b))
        ax.pie(
            sizes[i],
            wedgeprops={
                'edgecolor': 'yellow',
                'linewidth': 1,
                'linestyle': 'dotted',
                'facecolor':'none'
            }
        )
        fig_size_a += .5
        fig_size_b += .5
        ax.set_ylabel(f"{sizes_name_edge[1][i]} porciones", fontdict = {'fontsize': 12, 'fontweight':'bold', 'color':'tab:red'})
        ax.set_title(f"{sizes_name_edge[0][i]}".upper(), fontdict = {'fontsize': 12, 'fontweight':'bold', 'color':'tab:red'})
        ax.set_xlabel(f"<---------- {sizes_name_edge[2][i]} cm ---------->", fontdict = {'fontsize': 10, 'fontweight':'bold', 'color':'tab:red'})

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        bytes_array.append(img)
        plt.close(fig)

    base64_images = []
    for byte_img in bytes_array:
        base64_image = base64.b64encode(byte_img.getvalue()).decode('utf-8')
        base64_images.append(f"data:image/png;base64,{ base64_image }")
        
    return render(request, 'base.html', { 'images': base64_images })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
