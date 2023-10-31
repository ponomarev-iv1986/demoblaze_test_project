# Демонстрационный проект по тестированию UI и API сайта <a target="_blank" href="https://www.demoblaze.com">"Product Store"</a>

![This is an image](design/images/Main_page.png)

## Стек технологий:
<img src="design/icons/Python_logo_and_wordmark.svg" height="40" width="40" /><img src="design/icons/requests.png" height="40" width="40" /><img src="design/icons/Selenium.png" height="40" width="40" /><img src="design/icons/selene.png" height="40" width="40" /><img src="design/icons/Selenoid.svg" height="40" width="40" /><img src="design/icons/Pytest_logo.svg" height="40" width="40" /><img src="design/icons/Allure_Report.svg" height="40" width="40" /><img src="design/icons/Allure_EE.svg" height="40" width="40" /><img src="design/icons/Jenkins.svg" height="40" width="40" /><img src="design/icons/Docker.svg" height="40" width="40" /><img src="design/icons/Jira.svg" height="40" width="40" /><img src="design/icons/Telegram.svg" height="40" width="40" />

### Запуск автотеста производится удаленно на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a> при помощи написанной в Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev-IV-Demoblaze_Test/">джобы</a>.

## Для запуска автотестов необходимо:
- Открыть подготовленную <a target="_blank" href="https://jenkins.autotests.cloud/job/Ponomarev-IV-Demoblaze_Test/">джобу</a> в Jenkins
- Нажать "Build with Parameters" в боковом меню
- Ввести имя тестировщика
- Нажать Build

![This is an image](design/images/Start_job.png)

## После прохождения автотестов можно зайти в Allure Report и посмотреть отчет по тестовому прогону:
![This is an image](design/images/Allure_report_1.png)

## А так же подробно посмотреть результат прохождения каждого отдельного теста:
![This is an image](design/images/Allure_report_2.png)

## Полная статистика по тестовым прогонам, включая ручные тесты, хранятся в <a target="_blank" href="https://allure.autotests.cloud/project/3738/dashboards">Allure TestOps</a>.
### *Главный дашборд Allure TestOps:*
![This is an image](design/images/Allure_testops_dashboards.png)
### *Общий список автоматизированных и ручных тест-кейсов проекта:*
![This is an image](design/images/Allure_testops_test_cases.png)
### *Запуски автоматизированных и ручных тестов проекта:*
![This is an image](design/images/Allure_testops_launches.png)

## Тест-кейсы проекта и результаты тестовых прогонов интегрированы с <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-925">Atlassian Jira</a>.
![This is an image](design/images/Jira.png)

## Для мгновенного получения результатов о тестировании настроено автоматическое оповещение через Telegram.
![This is an image](design/images/Telegram.png)

## Ниже на видео представлен пример короткого теста на сервере <a target="_blank" href="https://selenoid.autotests.cloud/#/">Selenoid</a>.
![Watch the video](design/gif/test_video_example.gif)