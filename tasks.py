tasks = []


def list_tasks():
    """
    Görevlerin tutulacağı listeyi ve mevcut görevleri döndüren temel fonksiyonu oluşturur.
    """
    return tasks

def add_task(title):
    task = {"id": len(tasks) + 1, "title": title, "completed": False}
    tasks.append(task)
    return task
