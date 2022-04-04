select rp.*,
       coalesce((rp.resale_price / rpi.rebased_to_latest * 100),rp.resale_price) as resale_price_norm,
       coalesce((rp.price_per_sq_ft / rpi.rebased_to_latest * 100),rp.price_per_sq_ft) as price_per_sq_ft_norm,
       coalesce((rp.price_per_sq_ft_per_lease_yr / rpi.rebased_to_latest * 100),rp.price_per_sq_ft_per_lease_yr) as price_per_sq_ft_per_lease_yr_norm,
       coalesce((rp.price_per_sq_m / rpi.rebased_to_latest * 100), rp.price_per_sq_m) as price_per_sq_m_norm,
       coalesce((rp.price_per_sq_m_per_lease_yr / rpi.rebased_to_latest * 100),rp.price_per_sq_m_per_lease_yr) as price_per_sq_m_per_lease_yr_norm
from resale_prices_full rp
         left outer join resale_price_index_rebased rpi
                         on extract(quarter from rp.month) = right(rpi.quarter, 1)::int8
                             and extract(year from rp.month) = left(rpi.quarter, 4)::int8
;