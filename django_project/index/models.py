from django.db import models
from django.core.cache import cache
from django.utils import timezone

class index(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)  # Resim güncellendiğinde otomatik olarak tarih ve saat güncellenir

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Resim güncellendiğinde last_updated alanını güncelle
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)
        
        # Önbelleği güncelle

    def update_cache(self):
        # Önbelleği güncelleme işlemini burada gerçekleştir
        data_from_db = index.objects.all()  # Tüm verileri yeniden çek
        cache.set("my_key", data_from_db, timeout=1)  # Önbelleği güncelle

    class Meta:
        verbose_name = "index"
        verbose_name_plural = "index"
        ordering = ['-id']
