from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Nomor Telepon", blank=True, null=True)
    subject = models.CharField(max_length=150, verbose_name="Subjek", blank=True, null=True)
    message = models.TextField(verbose_name="Pesan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat Pada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Diperbarui Pada")

    class Meta:
        verbose_name = "Kontak"
        verbose_name_plural = "Kontak"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"