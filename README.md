# Демонстрационный проект по тестированию UI и API сайта <a target="_blank" href="https://www.demoblaze.com">"Product Store"</a>

![This is an image](design/images/main_page.png)

## Стек технологий:
<img src="design/icons/python_logo_and_wordmark.svg" height="40" width="40" /><img src="design/icons/requests.png" height="40" width="40" /><img src="design/icons/selenium.png" height="40" width="40" /><img src="design/icons/selene.png" height="40" width="40" /><img src="design/icons/selenoid.svg" height="40" width="40" /><img src="design/icons/pytest_logo.svg" height="40" width="40" /><img src="design/icons/allure_Report.svg" height="40" width="40" /><img src="design/icons/allure_EE.svg" height="40" width="40" /><img src="design/icons/jenkins.svg" height="40" width="40" /><img src="design/icons/docker.svg" height="40" width="40" /><img src="design/icons/jira.svg" height="40" width="40" /><img src="design/icons/telegram.svg" height="40" width="40" />

### Запуск автотеста производится удаленно на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a> при помощи написанной в Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev-IV-Demoblaze_Test/">джобы</a>.

## Для запуска автотестов необходимо:
- Открыть подготовленную <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev-IV-Demoblaze_Test/">джобу</a> в Jenkins
- Нажать "Build with Parameters" в боковом меню
- Ввести имя тестировщика
- Нажать Build

![This is an image](design/images/start_job.png)

## После прохождения автотестов можно зайти в Allure Report и посмотреть отчет по тестовому прогону:
![This is an image](design/images/allure_report_1.png)

## А так же подробно посмотреть результат прохождения каждого отдельного теста:
![This is an image](design/images/allure_report_2.png)

## Полная статистика по тестовым прогонам, включая ручные тесты, хранятся в <a target="_blank" href="https://allure.autotests.cloud/project/3738/dashboards">Allure TestOps</a>.
### *Главный дашборд Allure TestOps:*
![This is an image](design/images/allure_testops_dashboards.png)
### *Общий список автоматизированных и ручных тест-кейсов проекта:*
![This is an image](design/images/allure_testops_test_cases.png)
### *Запуски автоматизированных и ручных тестов проекта:*
![This is an image](design/images/allure_testops_launches.png)

## Тест-кейсы проекта и результаты тестовых прогонов интегрированы с <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-925">Atlassian Jira</a>.
![This is an image](design/images/jira.png)

## Для мгновенного получения результатов о тестировании настроено автоматическое оповещение через Telegram.
![This is an image](design/images/telegram.png)

## Ниже на видео представлен пример короткого теста на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a>.
![Watch the video](design/gif/test_video_example.gif)