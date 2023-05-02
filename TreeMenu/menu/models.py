from django.db import models
"""Класс список меню"""
class ListMenu(models.Model):
    name = models.CharField('Название', max_length=150)
    position=models.IntegerField('Позиция', default=1)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
"""Класс Меню"""
class MenuItem(models.Model):
    menu = models.ForeignKey(
        ListMenu, on_delete=models.CASCADE, related_name='items',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        verbose_name='Родитель', blank=True, null=True
    )
    name = models.CharField('Название', max_length=150)
    """Поле позиция представляет сквозную нумерацию пунктов меню"""
    position = models.IntegerField('Позиция', default=1)


    @property
    def level(self):
        if self.parent:
            return self.parent.level + 1
        return 1

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name