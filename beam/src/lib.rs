use std::error::Error;
use std::fs;


pub struct Config {
    pub file_path: String,
}


impl Config {

     pub  fn build(args: &[String]) -> Result<Config, &'static str> {
          if args.len() < 2 {
             return Err("usage: beam inputfile");
         }

         let file_path = args[1].clone();
         Ok(Config{file_path})
     }
}

pub fn run(config: Config) ->Result<(), Box<dyn Error>> {
    println!("read file: {}", config.file_path);
    Ok(())
}
