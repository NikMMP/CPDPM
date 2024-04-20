use crate::krylov::*;
pub mod krylov;

use std::env;
use std::process;

use beam::Config;
use std::collections::HashMap;

fn main() {
       
    let args: Vec<String> = env::args().collect();
    //dbg!(args);
    let config = Config::build(&args).unwrap_or_else(|err| { println!("Problem parsing arguments: {err}");
                                                             process::exit(1);
                                                           }); 

   let mut n: u32 = 1;
   let EJ: f64 = 200000.0; 
   let m0: f64 = 500.0 ;
   let l : f64 = 2.0;

   let mut data = HashMap::new();

   if let Ok(lines) = beam::read_lines(config.file_path) {

      for line in lines.flatten() {
          //println!("{}", line);
          let words: Vec<&str> = line.split(',').collect();
          data.insert(String::from(words[0]),String::from(words[1]));
      }

   }
   
   for (key, value) in &data {
       println!("{key}: {value}");
   } 
    
   let pi: f64 = std::f64::consts::PI;

   let dx: f64 = 0.01;
   let mut x: f64 = 0.0;
  
   n = 2;
   let alpha: f64 = alpha_n(n) / l;
   let freq: f64 = alpha * alpha / ( 2.0 * pi) * (EJ / m0).sqrt();
   println!("Frequency, Hz: {freq}");
   println!("Mode shape:");

   while x < l {
      let v = -K4(alpha * l) * K1(alpha * x) + K3(alpha * l) * K2(alpha * x);
      println!("{x}   {v}");
      x += dx;
   }
}
