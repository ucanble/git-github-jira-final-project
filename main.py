from tasks import list_tasks, add_task

add_task("Github ve jira entegrasonunu tamamla")
add_task("final proje dokümantasyonunu hazırla")

for task in list_tasks():
    status = "tamamlandı" if task["completed"] else "bekliyor"
    print(f"{task["id"]}. {task["title"]} - {status}")

