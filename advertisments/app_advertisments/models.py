from django.db import models

class Advertisment(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена",max_length=10, decimal_places=2, max_digits=20)
    action = models.BooleanField("торг", help_text="отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price: .2f})>"