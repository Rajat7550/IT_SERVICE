from decimal import Decimal

from django.db import models

class Service(models.Model):
    SERVICE_NAME = [
        ('Web Development', 'Web Development'),
        ('Mobile Development', 'Mobile Development'),
        ('Cloud Services', 'Cloud Services'),
        ('Data Analytics', 'Data Analytics'),
        ('Cyber Security', 'Cyber Security'),
        ('Networking', 'Networking'),
        ('IT Support', 'IT Support'),
        ('AI & Machine Learning', 'AI & Machine Learning'),
        ('DevOps', 'DevOps'),
        ('Consulting', 'Consulting'),
    ]

    PAYMENT_TERMS = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
    ]

    SERVICE_PACKAGES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    payment_terms = models.CharField(max_length=100, choices=PAYMENT_TERMS,null=True)
    service_package = models.CharField(max_length=100, choices=SERVICE_PACKAGES,null=True)
    service_name = models.CharField(max_length=100,choices=SERVICE_NAME,null=True)
    service_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    service_tax = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    service_image = models.ImageField(upload_to='services/')
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.service_tax = self.service_price * Decimal('0.18')
        super(Service, self).save(*args, **kwargs)
    @property
    def total_price(self):
        return self.service_price + self.service_tax