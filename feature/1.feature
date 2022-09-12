Feature: Test

    Scenario: Write test-case via Gherkin
        Given Open the browser and expand to full screen
        When Go to the yandex.ru page
        When In the "Market" section choose "Smartphones"
        When Open "All filters"
        When Choose price under 2000 rubles and screen size from 3 inches
        When  Choose 5 producers
        When Press the "Show" button
        When Count the number of producers on the page
        When Remember the last smartphone in the page
        When Change sort by price
        When Find and click to the name of smartphone in the memory
        When Show rating of the smartphone
        Then Quit the browser
