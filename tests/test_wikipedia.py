import pytest

MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"
ARTICLE = "https://en.wikipedia.org/wiki/Alan_Turing"


def run(ai_agent, goal, url):
    passed, log = ai_agent(goal, url)
    assert passed, "\n".join(log)


def test_main_page_loads(ai_agent):
    run(ai_agent, "Verify 'Welcome to Wikipedia' is shown", MAIN_PAGE)


def test_article_page_content(ai_agent):
    run(ai_agent,
        "Verify 'Alan Turing' is shown, then verify 'Bletchley Park' is shown",
        ARTICLE)


def test_search_for_article(ai_agent):
    run(ai_agent,
        "Type 'Alan Turing' into the 'Search' field, then click 'Search', "
        "then verify 'Bletchley Park' is shown",
        MAIN_PAGE)