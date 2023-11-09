-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Identifying crime ID:
SELECT *
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Crime id 295. Theft took place at 10:15am at Humphrey Street Bakery, there're three witnesses.

-- Researching interviews:
SELECT *
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28;

-- Interviews 161, 162 and 163 found useful.
    -- 161 says the thief got into a car sometime within 10min after the theft. Look security footage of bakery parking lot between 10:15 and 10:25am.
    -- 162 says the thief withdrew money from the ATM at Leggett Street earlier that morning.
    -- 163 says the thief called someone on the phone during less that 1 minute in the parking lot. He told the other person to purchase the earliest flight out of town at the next morning.

-- Researching ATM withdrawals that day:
SELECT name
FROM people AS p
JOIN bank_accounts AS ba ON ba.person_id = p.id
JOIN atm_transactions AS atm ON atm.account_number = ba.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- 8 people withdraw money in the Leggett Street ATM that day:

-- Suspects:
    -- Bruce
    -- Diana
    -- Brooke
    -- Kenny
    -- Iman
    -- Luca
    -- Taylor
    -- Benista

-- Researching who of those eight suspects made phone calls of the specified duration that same day:

SELECT name
FROM people AS p
JOIN phone_calls AS pc ON p.phone_number = pc.caller
WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60 AND p.name IN
    (SELECT name
    FROM people AS p
    JOIN bank_accounts AS ba ON ba.person_id = p.id
    JOIN atm_transactions AS atm ON atm.account_number = ba.account_number
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');

-- 5 suspects left:
    -- Bruce
    -- Taylor
    -- Diana
    -- Kenny
    -- Benista

-- Retrieving license plates of the five remaining suspects:

SELECT license_plate
FROM people
WHERE name IN
    (SELECT name
    FROM people AS p
    JOIN phone_calls AS pc ON p.phone_number = pc.caller
    WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60 AND p.name IN
        (SELECT name
        FROM people AS p
        JOIN bank_accounts AS ba ON ba.person_id = p.id
        JOIN atm_transactions AS atm ON atm.account_number = ba.account_number
        WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'));

-- Checking people that made an ATM withdraw that morning, made a phone call of less that 1 minute and abandoned bakery parking between 10:15 and 10:25:

SELECT name
FROM people AS p
JOIN bakery_security_logs AS bsl ON bsl.license_plate = p.license_plate
WHERE bsl.hour = 10 AND bsl.minute >= 15 AND bsl.minute <= 25 AND p.license_plate IN
    (SELECT license_plate
    FROM people
    WHERE name IN
        (SELECT name
        FROM people AS p
        JOIN phone_calls AS pc ON p.phone_number = pc.caller
        WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60 AND p.name IN
            (SELECT name
            FROM people AS p
            JOIN bank_accounts AS ba ON ba.person_id = p.id
            JOIN atm_transactions AS atm ON atm.account_number = ba.account_number
            WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')));

-- Two suspects: Bruce (5773159633 passport) and Diana (3592750733 passport).
SELECT *
FROM phone_calls AS pc
JOIN people AS p ON p.phone_number = pc.caller
WHERE (p.name = 'Bruce' OR p.name = 'Diana') AND (pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60);

-- Bruce called (375) 555-8161.
SELECT name, passport_number
FROM people
WHERE phone_number = '(375) 555-8161';
-- (375) 555-8161 is Robin, who has no passport (suspiccious).

-- Diana called (725) 555-3243.
SELECT name, passport_number
FROM people
WHERE phone_number = '(725) 555-3243';
-- (725) 555-3243 is Philip, passport 3391710505.

-- Identifying earliest flight out of town next day (29th)
SELECT id
FROM flights
WHERE year = 2021 AND month = 7 AND day = 29
ORDER BY hour, minute LIMIT 1;

-- Earliest flight ID out of town: 36

-- Searching Bruce and Diana in that flight:
SELECT p.name
FROM people AS p
JOIN passengers AS ps ON p.passport_number = ps.passport_number
JOIN flights AS f ON f.id = ps.flight_id
WHERE f.id = 36 AND p.passport_number IN (5773159633, 3592750733);

-- Only Bruce was in that flight. Bruce is the thief, and Robin is the accomplice.

-- Retrieving flight destination:
SELECT city
FROM airports AS ap
JOIN flights AS f ON f.destination_airport_id = ap.id
WHERE f.id = 36;

-- Bruce escaped to NYC.
