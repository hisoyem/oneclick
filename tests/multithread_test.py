from threading import Thread, Barrier

from selenium import webdriver


# -
def func(barrier):
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element_by_id("email").send_keys("xx")
    driver.find_element_by_id("pass").send_keys("yy")
    b = driver.find_element_by_id("loginbutton")

    print('wait for others')
    barrier.wait()

    print('click')
    b.click()


# ---

url = 'https://www.facebook.com/'

number_of_threads = 3

barrier = Barrier(number_of_threads)

threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
