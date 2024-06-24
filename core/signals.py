import os
import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Movie
from core.tasks import convert_480p, convert_720p

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Movie)
def video_post_save(sender, instance, created, **kwargs):
    logger.info("Video wurde gespeichert")
    logger.info(f"Created: {created}, Instance ID: {instance.id}")
    if created:
        logger.info("New video created")
        video_480p_path = convert_480p(instance.video_file.path)
        video_720p_path = convert_720p(instance.video_file.path)
        instance.video_480p = video_480p_path.replace(instance.video_file.path.rsplit('/', 1)[0], 'videos').replace('\\', '/')
        instance.video_720p = video_720p_path.replace(instance.video_file.path.rsplit('/', 1)[0], 'videos').replace('\\', '/')
        instance.save()
    else:
        logger.info("Video updated, skipping conversion")

@receiver(post_delete, sender=Movie)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    logger.info("Deleting video file")
    if instance.video_file:
        # Delete the original file
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)

        # Delete the converted files
        file_root, file_ext = os.path.splitext(instance.video_file.path)
        converted_480p = f"{file_root}_480p.mp4"
        converted_720p = f"{file_root}_720p.mp4"

        if os.path.isfile(converted_480p):
            os.remove(converted_480p)

        if os.path.isfile(converted_720p):
            os.remove(converted_720p)
