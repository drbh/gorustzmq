//
//  Pubsub envelope subscriber.
//

package main

import (
	zmq "github.com/pebbe/zmq4"

	"fmt"
	"time"
)

func main() {
	//  Prepare our subscriber
	subscriber, _ := zmq.NewSocket(zmq.SUB)
	defer subscriber.Close()

	time.Sleep(1000 * time.Millisecond)

	subscriber.Connect("tcp://*:5555")
	subscriber.SetSubscribe("")

	for {
		// Read envelope with address
		address, _ := subscriber.Recv(0)
		fmt.Println(address)
	}
}
