from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
We can display all properties listed with Makers BnB
"""

def test_get_all_spaces(db_connection, web_client):
    db_connection.seed("seeds/makersbnb.sql")
    get_response = web_client.get("/spaces?spacename")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Space(1, danHouse, Located on the Beach, 20, 1), Space(2, khalifaHouse, Central Location, 15, 2), Space(3, tomHouse, toursity location, 80, 3), Space(4, lilyHouse, located in a lovely touristy village, 90, 4)'
    
    
    
    