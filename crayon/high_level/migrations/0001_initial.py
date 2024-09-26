# Generated by Django 4.2.16 on 2024-09-26 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Etape",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("duree", models.IntegerField()),
                (
                    "etape_suivante",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.etape",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("prix", models.IntegerField()),
                ("n_serie", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Ressource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("prix", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ville",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("code_postal", models.IntegerField()),
                ("prix_m2", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Usine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("surface", models.IntegerField()),
                ("machines", models.ManyToManyField(to="high_level.machine")),
                (
                    "ville",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.ville",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.IntegerField()),
                (
                    "ressource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.ressource",
                    ),
                ),
                (
                    "usine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.usine",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SiegeSocial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("surface", models.IntegerField()),
                (
                    "ville",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.ville",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="QuantiteRessource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantite", models.IntegerField()),
                (
                    "ressource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.ressource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Produit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("prix", models.IntegerField()),
                (
                    "premiere_etape",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.etape",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="etape",
            name="machine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="high_level.machine"
            ),
        ),
        migrations.AddField(
            model_name="etape",
            name="quantite_ressource",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="high_level.quantiteressource",
            ),
        ),
    ]
