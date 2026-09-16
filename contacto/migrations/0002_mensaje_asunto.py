from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mensaje",
            name="asunto",
            field=models.CharField(default="", max_length=150),
            preserve_default=False,
        ),
    ]