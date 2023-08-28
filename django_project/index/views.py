from django.shortcuts import render
from django.views import View
from django.core.cache import cache
from django.http import HttpResponse
from django.utils import timezone
from .models import index  # Doğru model adını kullandığınızdan emin olun
import time

class IndexView(View):

    def get_data_from_database(self):
        data_from_db = index.objects.all()
        print("Veritabanından veri çekildi")
        return data_from_db
    

    def get(self, request, *args, **kwargs):
        cached_data = cache.get("my_key")
        
        if cached_data is None:    # Önbellekte veri yoksa
            start_time = timezone.now() # Zamanı başlat
            data_from_db = self.get_data_from_database() # Veritabanından veri çek
            elapsed_time = (timezone.now() - start_time).total_seconds() # Saniye cinsinden geçen süre
            
            if elapsed_time > 4: # Eğer veritabanından veri çekme süresi 4 saniyeyi geçerse
                last_cached_data = cache.get("my_key") # Son önbelleklenen veriyi al
                if last_cached_data is not None: # Eğer son önbelleklenen veri varsa
                    return HttpResponse(last_cached_data) # Son önbelleklenen veriyi göster 
                return HttpResponse("Veritabanı ve önbellek boş") # Eğer son önbelleklenen veri yoksa
            
            cached_data = data_from_db # Eğer veritabanından veri çekme süresi 4 saniyeyi geçmiyorsa
            cache.set("my_key", cached_data, timeout=1) # 1 saniye önbellekte tutulacak
        
        context = { # Veriyi göstermek  için context oluştur
            'data': cached_data, # Önbellekten veriyi al
        }

        return render(request, 'index.html', context) # Veriyi göster 
    


    # def post(self, request, *args, **kwargs):
    #     # Resim güncellendiğinde veya yeni resim yüklendiğinde
    #     self.update_cache()
    #     return HttpResponse("Önbellek güncellendi")



    

class OtherPageView(View):
    
    def get(self, request, *args, **kwargs):
        new_data = ["Yeni veri 1", "Yeni veri 2"]  # Eklenecek yeni verileri buraya ekleyin
        
        # Önbelleği güncelleme işlemini burada gerçekleştir
        cached_data = cache.get("my_key")
        if cached_data is None:
            cached_data = []

        # Sadece yeni verileri önbelleğe ekleyin
        cached_data = new_data
        cache.set("my_key", cached_data, timeout=1)

        print("Önbelleğe yeni veri eklendi")
        print(cached_data)

        return render(request, 'other_page.html', {"data": cached_data})
