-- Question 3 a
select * from policy
where policy_inception_date > '2021-01-21';

-- Question 3 b
select policy.policy_number as 'Policy Number',
concat(policy_holder_first_name,' ',policy_holder_last_name) as 'Policy Holder Name',
claim_number as 'Claim Number'
from claim inner join policy on claim.policy_number=policy.policy_number;

-- Question 3 c
select policy.policy_number as 'Policy Number',
concat(policy_holder_first_name,' ',policy_holder_last_name) as 'Policy Holder Name',
sum_insured as 'Sum Insured'

from policy inner join policy_item on policy.policy_number=policy_item.policy_number;

    