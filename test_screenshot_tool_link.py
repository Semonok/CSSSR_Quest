def test_screenshot_tool_link(driver):
    expected_link = 'http://monosnap.com/'
    driver.find_element_by_link_text('НАХОДИТЬ НЕСОВЕРШЕНСТВА').click()
    real_link = driver.find_element_by_link_text('Софт для быстрого создания скриншотов').get_attribute('href')
    assert expected_link == real_link