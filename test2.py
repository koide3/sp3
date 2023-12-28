#!/usr/bin/python3
import astropy.coordinates
import astropy.time
import sp3

import scipy
from datetime import datetime, timedelta

def main():
  product = sp3.Product.from_file("test_products/emr21000.sp3")
  sv = product.satellite_with_id(b'G10')
  
  sv_locs, sv_clocks_drifts = sp3.itrs(
    id=sp3.Sp3Id("G28"),
    obstime=astropy.time.Time(
      [
        "2022-01-01T00:00:00.0000Z",
        "2022-01-01T00:05:00.0000Z"
      ],
    ),
    download_directory='/tmp/sp3_cache',
    interpolate_clock_bias=True
  )
  
  clight = 299792458.0
  e1 = 238.201060 / 1e6 - sv_clocks_drifts[1]
  print(e1, clight * e1)
  print(sv_clocks_drifts * 1e6)
  

if __name__ == '__main__':
  main()
