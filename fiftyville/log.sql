-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street" AND id = 295;
-- time 10:15 am, bakery
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND id BETWEEN 161 AND 164;
--after 10 min thief get into a car in the bakery parking, early in this moring ATM at Leggett Street withdrawing money, after leaving bakery call someone less than a minute\
-- planning to take earliest flight out of Fiftyvillie tomorrow, the thief asked the person purchase for flight ticket.
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;
SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25);
--|   id   |  name   |  phone_number  | passport_number | license_plate |
--+--------+---------+----------------+-----------------+---------------+
--| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
--| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
--| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
--| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
--| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
--| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
--| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
--+--------+---------+----------------+-----------------+---------------+
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25);

--ATM transactions in this morinig
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";
SELECT * FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw");
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
--|   id   |  name   |  phone_number  | passport_number | license_plate |
--+--------+---------+----------------+-----------------+---------------+
--| 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
--| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
--| 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       |
--| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
--| 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       |
--| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
--| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
--| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
--+--------+---------+----------------+-----------------+---------------+

--phone_calls
SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25)) AND duration < 60;
--| id  |     caller     |    receiver    | year | month | day | duration |
--+-----+----------------+----------------+------+-------+-----+----------+
--| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
--| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
--| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
--| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
--| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
--| 395 | (367) 555-5533 | (455) 555-5315 | 2021 | 7     | 30  | 31       |
--+-----+----------------+----------------+------+-------+-----+----------+
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25)) AND duration < 60);
--|   id   |  name  |  phone_number  | passport_number | license_plate |
--+--------+--------+----------------+-----------------+---------------+
--| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
--| 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       |
--| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
--+--------+--------+----------------+-----------------+---------------+

--FLIGHTS
-- investigate earliest flight
SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29;
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      |
--| 23 | 8                 | 11                     | 2021 | 7     | 29  | 12   | 15     |
--| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
--| 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     |
--| 53 | 8                 | 9                      | 2021 | 7     | 29  | 15   | 20     |
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--filght id = 36
SELECT * FROM airports WHERE id = 8
UNION SELECT * FROM airports WHERE id = 4;
--| id | abbreviation |          full_name          |     city      |
--+----+--------------+-----------------------------+---------------+
--| 4  | LGA          | LaGuardia Airport           | New York City |
--| 8  | CSF          | Fiftyville Regional Airport | Fiftyville    |
--+----+--------------+-----------------------------+---------------+

SELECT * FROM passengers WHERE flight_id = 36;

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
--|   id   |  name  |  phone_number  | passport_number | license_plate |
--+--------+--------+----------------+-----------------+---------------+
--| 395717 | Kenny  | (826) 555-1652 | 9878712108      | 30G67EN       |
--| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
--| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
--| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
--| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| 651714 | Edward | (328) 555-1152 | 1540955065      | 130LD9Z       |
--| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
--| 953679 | Doris  | (066) 555-9701 | 7214083635      | M51FA04       |
--+--------+--------+----------------+-----------------+---------------+
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);

--intersecting all cases and the thief is ......
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25)) AND duration < 60)
INTERSECT
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25)
INTERSECT
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
--| name  |
--+-------+
--| Bruce | == Thief
--+-------+
--finding FOR accomplice...
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND caller = "(367) 555-5533" AND duration < 60);
--| name  |
--+-------+
--| Robin |