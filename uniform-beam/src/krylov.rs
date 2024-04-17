fn K1(x: f64) -> f64 {
   0.5 * (x.cosh() + x.cos())
}


fn K2(x: f64) -> f64 {
   0.5 * (x.sinh() + x.sin())
}


fn K3(x: f64) -> f64 {
   0.5 * (x.cosh() - x.cos())
}



fn K4(x: f64) -> f64 {
   0.5 * (x.sinh() - x.sin())
}


fn power(a: i32, n: u32) -> i32 {
   let mut i = 0;
   let mut pw = 1;
   while i < n {
    pw *= a;
     i += 1;
   } 
   pw
}
