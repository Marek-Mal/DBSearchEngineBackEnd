from django.db import models

class wartsila_engine(models.Model):

    id = models.CharField(max_length=10, blank=False, null=False, primary_key=True, unique=True)
    component_name = models.CharField(max_length=100, blank=False, null=False)
    pdf_page = models.PositiveBigIntegerField(default=1, blank=False, null=False)
    engine = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.component_name} ({self.engine})"


class spare_parts(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    part_id = models.CharField(max_length=10, blank=True, null=True)
    part_name = models.CharField(max_length=255, blank=False, null=False)
    pdf_page = models.PositiveBigIntegerField(default=1, blank=False, null=False)
    price = models.PositiveIntegerField(default=100, blank=False, null=False)
    extras = models.CharField(max_length=255, blank=True, null=True)
    isAvalable = models.CharField(max_length=255, default="Currently in Storage", blank=True, null=True)
    component_id = models.ForeignKey(wartsila_engine, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.component_id:
            self.pdf_page = self.component_id.pdf_page + 1
        super(spare_parts, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.part_id} {self.part_name} (Page: {self.pdf_page})"

