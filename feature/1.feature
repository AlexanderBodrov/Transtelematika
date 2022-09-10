Feature: Test

    Scenario: Write test-case via Gherkin
        Given Open the browser and expand to full screen
        Then Go to the yandex.ru page
        And In the "Market" section choose "Smartphones"


        When Open "All filters"
        Then Choose price under 2000 rubles and screen size from 3 inches
        And  Choose 5 producers

        When Press the "Show" button
        Then Count the number of producers on the page
        And Remember the last smartphone in the page

        When Change sort by price
        Then Find and click to the name of smartphone in the memory
        And Show rating of the smartphone
        And Quit the browser
