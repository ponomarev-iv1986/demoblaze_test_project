from demoblaze_test_project.pages.index import Index

index = Index()


def test_phones_filter():
    index.open()

    index.click_phones()

    index.should_have_phones()
