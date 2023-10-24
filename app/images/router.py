import shutil

from fastapi import APIRouter, UploadFile

# from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)

@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    im_path = f"app/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        # Сохраняем файл в локальное хранилище (на практике обычно сохраняется в удаленное хранилище)
        shutil.copyfileobj(file.file, file_object)
    # Отдаем Celery фоновую задачу на обработку картинки
    # process_pic.delay(im_path)
