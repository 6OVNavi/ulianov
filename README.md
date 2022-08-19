# Решение на Ульяновскую обл Цифрового прорыва на 0.966 на паблике.

Для начала была обучена модель детекции номеров машин yolo5x на открытом коде и открытом датасете с каггла

![image](https://user-images.githubusercontent.com/59533921/184349767-ff833aae-95c4-4428-8775-db38758fa567.png)

*файл train plates detection содержит ссылку на каггл ноутбук*

Далее по немного измененному бейзлайну (*F1_detect_and_write.ipynb*) детектим сначала машины, а потом номера машин и сохраняем таблички с ббоксами.

Из-за того, что по неизвестным причинам yolo иногда не детектит жигули, пришлось доразметить руками тест (*fill_test_by_hand.py*)

Еще из-за некоторых проблем пришлось перевести картинки формата heic в формат jpg через сервис iloveimg

Далее я достаю общую exif информацию для iphone 11 и 12 и сохраняю эти таблички (*get_exif.py*)

По этим табличкам и идет обучение, в файле *for_exif* последней версии идут некоторые преобразования над табличными данными, обучается катбуст.
