USE `Constantia_Insurance_Assessment`;

CREATE TABLE `policy`(
    policy_number INT(4) NOT NULL,
    policy_holder_first_name VARCHAR(50) NOT NULL,
    policy_holder_last_name VARCHAR(50) NOT NULL,
    policy_inception_date DATE NOT NULL,
    PRIMARY KEY (policy_number)
);

CREATE TABLE policy_item(
    policy_number INT(4) NOT NULL,
    policy_item_number VARCHAR(50) NOT NULL,
    section VARCHAR(50) NOT NULL,
    sum_insured DECIMAL(18,0) NOT NULL,
    PRIMARY KEY (policy_item_number),
    FOREIGN KEY (policy_number) REFERENCES policy(policy_number)
);

CREATE TABLE claim(
    claim_number VARCHAR(6) NOT NULL,
    policy_number INT(4) NOT NULL,
    date_of_loss DATE NOT NULL,
    claim_rate_reported DATE NOT NULL,
    PRIMARY KEY (claim_number),
    FOREIGN KEY (policy_number) REFERENCES policy(policy_number)
    
);

