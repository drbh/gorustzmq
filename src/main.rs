use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let context = zmq::Context::new();
    let publisher = context.socket(zmq::PUB).unwrap();
    publisher
        .bind("tcp://127.0.0.1:5555")
        .expect("failed binding publisher");

    loop {
        let start = SystemTime::now();
        let since_the_epoch = start
            .duration_since(UNIX_EPOCH)
            .expect("Time went backwards");
        let s = format!("{:?}", since_the_epoch);
        publisher
            .send(&s, 0)
            .expect("failed sending first envelope");

        let mut child = Command::new("sleep").arg(".5").spawn().unwrap();
        let _result = child.wait().unwrap();
    }
}
