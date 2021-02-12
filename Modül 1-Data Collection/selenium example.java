package com.company;

import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.io.IOException;

public class App {
    private static final Logger log = LogManager.getLogger(App.class);

    public static void main(String[] args) throws IOException, InterruptedException {
        BasicConfigurator.configure();
        log.info("Get DOM via Jsoup");
        Document doc = Jsoup.connect("https://vatanbilgisayar.com/").get();
        log.info(doc.title());
        log.info(doc.getElementsByClass("brands"));

        log.info("Get DOM via Chromedriver");
        System.setProperty("webdriver.chrome.driver", "/usr/local/bin/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.get("https://vatanbilgisayar.com/");
        WebElement button = driver.findElement(By.id("btnMyAccount"));
        Thread.sleep(2000);
        button.click();
        log.info("My Account button is clicked");
        Thread.sleep(2000);
        driver.quit();

    }
}