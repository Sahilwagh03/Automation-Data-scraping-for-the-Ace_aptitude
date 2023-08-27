from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
import random


def determine_difficulty():
    difficulties = ["easy", "medium", "hard"]
    return random.choice(difficulties)

def scrape_questions_from_urls(urls):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument("--headless=new")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    
    all_questions = []  # List to store all scraped questions
    


    for index, url in enumerate(urls, start=1):
        driver.get(url)
        
        print(f"Scraping from URL {index}: {url}")

        if "problems-on-trains" in url:
            subtopic = "Problems on Trains"
        elif "time-and-distance" in url:
            subtopic = "Time and Distance"
        elif "height-and-distance" in url:
            subtopic = "Height and Distance"
        elif "time-and-work" in url:
            subtopic = "Time and Work"
        elif "simple-interest" in url:
            subtopic = "Simple Interest"
        elif "compound-interest" in url:
            subtopic = "Compound Interest"
        elif "profit-and-loss" in url:
            subtopic = "Profit and Loss"
        elif "partnership" in url:
            subtopic = "Partnership"
        elif "percentage" in url:
            subtopic = "Percentage"
        elif "problems-on-ages" in url:
            subtopic = "Problems on Ages"
        elif "calendar" in url:
            subtopic = "Calendar"
        elif "clock" in url:
            subtopic = "Clock"
        elif "average" in url:
            subtopic = "Average"
        elif "area" in url:
            subtopic = "Area"
        elif "volume-and-surface-area" in url:
            subtopic = "Volume and Surface Area"
        elif "permutation-and-combination" in url:
            subtopic = "Permutation and Combination"
        elif "numbers" in url:
            subtopic = "Numbers"
        elif "problems-on-numbers" in url:
            subtopic = "Problems on Numbers"
        elif "problems-on-hcf-and-lcm" in url:
            subtopic = "Problems on H.C.F and L.C.M"
        elif "decimal-fraction" in url:
            subtopic = "Decimal Fraction"
        elif "simplification" in url:
            subtopic = "Simplification"
        elif "square-root-and-cube-root" in url:
            subtopic = "Square Root and Cube Root"
        elif "surds-and-indices" in url:
            subtopic = "Surds and Indices"
        elif "ratio-and-proportion" in url:
            subtopic = "Ratio and Proportion"
        elif "chain-rule" in url:
            subtopic = "Chain Rule"
        elif "pipes-and-cistern" in url:
            subtopic = "Pipes and Cistern"
        elif "boats-and-streams" in url:
            subtopic = "Boats and Streams"
        elif "alligation-or-mixture" in url:
            subtopic = "Alligation or Mixture"
        elif "logarithm" in url:
            subtopic = "Logarithm"
        elif "races-and-games" in url:
            subtopic = "Races and Games"
        elif "stocks-and-shares" in url:
            subtopic = "Stocks and Shares"
        elif "probability" in url:
            subtopic = "Probability"
        elif "true-discount" in url:
            subtopic = "True Discount"
        elif "bankers-discount" in url:
            subtopic = "Banker's Discount"
        elif "odd-man-out-and-series" in url:
            subtopic = "Odd Man Out and Series"

        for number in range(1, 10):
            Question = driver.find_elements(By.XPATH, f"/html/body/main/section/div/div[2]/div[1]/div/div[2]/div[{number}]/div[1]/div[2]")


            # Extract correct answer using JavaScript execution
            correct_answer_element = driver.find_element(By.XPATH, f'/html/body/main/section/div/div[2]/div[1]/div/div[2]/div['+str(number)+']/div[3]/div[1]/div[1]/div[2]/span')
            correct_answer_unicode = driver.execute_script("return window.getComputedStyle(arguments[0], '::before').content;", correct_answer_element)
            print(correct_answer_unicode)

            # Count the number of option elements
            num_options = len(driver.find_elements(By.XPATH, f'/html/body/main/section/div/div[2]/div[1]/div/div[2]/div[{number}]/div[2]/div'))
                
            
            # Check if the question has exactly 4 options
            if num_options == 4:
                question_data = {}  # Dictionary to store question data
                
                # Extract question text
                for Question_element in Question:
                    question_data["questionText"] = Question_element.text
                
                options = []
                for x in range(1, 5):
                    option_elements = driver.find_elements(By.XPATH, f'/html/body/main/section/div/div[2]/div[1]/div/div[2]/div[{number}]/div[2]/div[{x}]/div[2]/div')
                    
                    # Iterate through the list of option elements and extract text
                    for option_element in option_elements:
                        option_text = option_element.text


                        # Check if the option is not "None of these"
                        if option_text != "None of these":
                            options.append(option_text)
                
                question_data["options"] = options
                
                # Determine the correct option based on specific criteria
                question_data["correctOption"] = ""
                
                # Determine the difficulty randomly
                question_data["difficulty"] = determine_difficulty()
                
                question_data["category"] = "General Aptitude"
                question_data["subtopic"] = subtopic
                
                all_questions.append(question_data)
        
        print(f"Finished scraping from URL {index}")
        print("-" * 40)  # Print a separator between different URLs
        
    driver.quit()
    return all_questions
    
if __name__ == "__main__":
    urls_to_scrape_trains = [
        "https://www.indiabix.com/aptitude/problems-on-trains/",
        "https://www.indiabix.com/aptitude/problems-on-trains/038002",
        "https://www.indiabix.com/aptitude/problems-on-trains/038003",
        "https://www.indiabix.com/aptitude/problems-on-trains/038004",
        "https://www.indiabix.com/aptitude/problems-on-trains/038005",
        "https://www.indiabix.com/aptitude/problems-on-trains/038006",
        "https://www.indiabix.com/aptitude/problems-on-trains/038007"
    ]

    urls_to_scrape_distance = [
        "https://www.indiabix.com/aptitude/time-and-distance/",
        "https://www.indiabix.com/aptitude/time-and-distance/036002",
        "https://www.indiabix.com/aptitude/time-and-distance/036003",
    ]

    urls_to_scrape_Height_and_Distance = [
        "https://www.indiabix.com/aptitude/time-and-distance/",
    ]

    urls_to_scrape_Time_and_Work = [
        "https://www.indiabix.com/aptitude/time-and-work/",
    ]

    urls_to_scrape_Simple_Interest = [
        "https://www.indiabix.com/aptitude/simple-interest/",
    ]

    urls_to_scrape_Compound_Interest = [
        "https://www.indiabix.com/aptitude/compound-interest/",
    ]

    urls_to_scrape_Profit_and_Loss = [
        "https://www.indiabix.com/aptitude/profit-and-loss/",
    ]

    urls_to_scrape_Partnership = [
    "https://www.indiabix.com/aptitude/partnership/",
    ]

    urls_to_scrape_Percentage = [
        "https://www.indiabix.com/aptitude/percentage/",
    ]


    urls_to_scrape_Races_and_Games = [
        "https://www.indiabix.com/aptitude/races-and-games/",
    ]

    urls_to_scrape_Stocks_and_Shares = [
        "https://www.indiabix.com/aptitude/stocks-and-shares/",
    ]

    urls_to_scrape_Probability = [
        "https://www.indiabix.com/aptitude/probability/",
    ]

    urls_to_scrape_True_Discount = [
        "https://www.indiabix.com/aptitude/true-discount/",
    ]

    urls_to_scrape_Bankers_Discount = [
        "https://www.indiabix.com/aptitude/bankers-discount/",
    ]

    urls_to_scrape_Odd_Man_Out_and_Series = [
        "https://www.indiabix.com/aptitude/odd-man-out-and-series/",
    ]

    urls_to_scrape_Area = [
        "https://www.indiabix.com/aptitude/area/",
    ]

    urls_to_scrape_Volume_and_Surface_Area = [
        "https://www.indiabix.com/aptitude/volume-and-surface-area/",
    ]

    urls_to_scrape_Permutation_and_Combination = [
        "https://www.indiabix.com/aptitude/permutation-and-combination/",
    ]

    urls_to_scrape_Numbers = [
        "https://www.indiabix.com/aptitude/numbers/",
    ]

    urls_to_scrape_Problems_on_Numbers = [
        "https://www.indiabix.com/aptitude/problems-on-numbers/",
    ]

    urls_to_scrape_Problems_on_HCF_and_LCM = [
        "https://www.indiabix.com/aptitude/problems-on-hcf-and-lcm/",
    ]

    urls_to_scrape_Decimal_Fraction = [
        "https://www.indiabix.com/aptitude/decimal-fraction/",
    ]

    urls_to_scrape_Simplification = [
        "https://www.indiabix.com/aptitude/simplification/",
    ]

    urls_to_scrape_Square_Root_and_Cube_Root = [
        "https://www.indiabix.com/aptitude/square-root-and-cube-root/",
    ]

    urls_to_scrape_Surds_and_Indices = [
        "https://www.indiabix.com/aptitude/surds-and-indices/",
    ]

    urls_to_scrape_Ratio_and_Proportion = [
        "https://www.indiabix.com/aptitude/ratio-and-proportion/",
    ]

    urls_to_scrape_Chain_Rule = [
        "https://www.indiabix.com/aptitude/chain-rule/",
    ]

    urls_to_scrape_Pipes_and_Cistern = [
        "https://www.indiabix.com/aptitude/pipes-and-cistern/",
    ]

    urls_to_scrape_Boats_and_Streams = [
        "https://www.indiabix.com/aptitude/boats-and-streams/",
    ]

    urls_to_scrape_Alligation_or_Mixture = [
        "https://www.indiabix.com/aptitude/alligation-or-mixture/",
    ]

    urls_to_scrape_Logarithm = [
        "https://www.indiabix.com/aptitude/logarithm/",
    ]


    urls_to_scrape_Calendar = [
        "https://www.indiabix.com/aptitude/calendar/",
    ]

    urls_to_scrape_Clock = [
        "https://www.indiabix.com/aptitude/clock/",
    ]

    urls_to_scrape_Average = [
        "https://www.indiabix.com/aptitude/average/",
    ]




    # Scrape questions for each topic
    all_questions_trains = scrape_questions_from_urls(urls_to_scrape_trains)
    # all_questions_distance = scrape_questions_from_urls(urls_to_scrape_distance)
    # all_questions_height_and_distance = scrape_questions_from_urls(urls_to_scrape_Height_and_Distance)
    # all_questions_time_and_work = scrape_questions_from_urls(urls_to_scrape_Time_and_Work)
    # all_questions_simple_interest = scrape_questions_from_urls(urls_to_scrape_Simple_Interest)
    # all_questions_compound_interest = scrape_questions_from_urls(urls_to_scrape_Compound_Interest)
    # all_questions_profit_and_loss = scrape_questions_from_urls(urls_to_scrape_Profit_and_Loss)
    # all_questions_partnership = scrape_questions_from_urls(urls_to_scrape_Partnership)
    # all_questions_percentage = scrape_questions_from_urls(urls_to_scrape_Percentage)
    # all_questions_races_and_games = scrape_questions_from_urls(urls_to_scrape_Races_and_Games)
    # all_questions_stocks_and_shares = scrape_questions_from_urls(urls_to_scrape_Stocks_and_Shares)
    # all_questions_probability = scrape_questions_from_urls(urls_to_scrape_Probability)
    # all_questions_true_discount = scrape_questions_from_urls(urls_to_scrape_True_Discount)
    # all_questions_bankers_discount = scrape_questions_from_urls(urls_to_scrape_Bankers_Discount)
    # all_questions_odd_man_out_and_series = scrape_questions_from_urls(urls_to_scrape_Odd_Man_Out_and_Series)
    # all_questions_area = scrape_questions_from_urls(urls_to_scrape_Area)
    # all_questions_volume_and_surface_area = scrape_questions_from_urls(urls_to_scrape_Volume_and_Surface_Area)
    # all_questions_permutation_and_combination = scrape_questions_from_urls(urls_to_scrape_Permutation_and_Combination)
    # all_questions_numbers = scrape_questions_from_urls(urls_to_scrape_Numbers)
    # all_questions_problems_on_numbers = scrape_questions_from_urls(urls_to_scrape_Problems_on_Numbers)
    # all_questions_problems_on_hcf_and_lcm = scrape_questions_from_urls(urls_to_scrape_Problems_on_HCF_and_LCM)
    # all_questions_decimal_fraction = scrape_questions_from_urls(urls_to_scrape_Decimal_Fraction)
    # all_questions_simplification = scrape_questions_from_urls(urls_to_scrape_Simplification)
    # all_questions_square_root_and_cube_root = scrape_questions_from_urls(urls_to_scrape_Square_Root_and_Cube_Root)
    # all_questions_surds_and_indices = scrape_questions_from_urls(urls_to_scrape_Surds_and_Indices)
    # all_questions_ratio_and_proportion = scrape_questions_from_urls(urls_to_scrape_Ratio_and_Proportion)
    # all_questions_chain_rule = scrape_questions_from_urls(urls_to_scrape_Chain_Rule)
    # all_questions_pipes_and_cistern = scrape_questions_from_urls(urls_to_scrape_Pipes_and_Cistern)
    # all_questions_boats_and_streams = scrape_questions_from_urls(urls_to_scrape_Boats_and_Streams)
    # all_questions_alligation_or_mixture = scrape_questions_from_urls(urls_to_scrape_Alligation_or_Mixture)
    # all_questions_logarithm = scrape_questions_from_urls(urls_to_scrape_Logarithm)
    # all_questions_calendar = scrape_questions_from_urls(urls_to_scrape_Calendar)
    # all_questions_clock = scrape_questions_from_urls(urls_to_scrape_Clock)
    # all_questions_average = scrape_questions_from_urls(urls_to_scrape_Average)

    # Combine all the scraped questions into one list
    all_questions = (
        all_questions_trains 
        # all_questions_distance +
        # all_questions_height_and_distance +
        # all_questions_time_and_work +
        # all_questions_simple_interest +
        # all_questions_compound_interest +
        # all_questions_profit_and_loss +
        # all_questions_partnership +
        # all_questions_percentage +
        # all_questions_races_and_games +
        # all_questions_stocks_and_shares +
        # all_questions_probability +
        # all_questions_true_discount +
        # all_questions_bankers_discount +
        # all_questions_odd_man_out_and_series +
        # all_questions_area +
        # all_questions_volume_and_surface_area +
        # all_questions_permutation_and_combination +
        # all_questions_numbers +
        # all_questions_problems_on_numbers +
        # all_questions_problems_on_hcf_and_lcm +
        # all_questions_decimal_fraction +
        # all_questions_simplification +
        # all_questions_square_root_and_cube_root +
        # all_questions_surds_and_indices +
        # all_questions_ratio_and_proportion +
        # all_questions_chain_rule +
        # all_questions_pipes_and_cistern +
        # all_questions_boats_and_streams +
        # all_questions_alligation_or_mixture +
        # all_questions_logarithm +
        # all_questions_calendar +
        # all_questions_clock +
        # all_questions_average
    )


    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(all_questions, indent=4)
    with open("questions.json", "w") as json_file:
        json_file.write(json_data)