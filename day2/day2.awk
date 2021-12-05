#!/bin/awk -f
BEGIN{
    xpos = 0;
    depth = 0;
    aim = 0;
}
{
    command = $1
    no = int($2)
    if(command == "forward")
    {
        xpos += no;
        depth += aim*no;
    }
    else if(command == "up")
    {
        aim -= no;
    }
    else {
        aim += no;
    }
}
END{
    print(xpos,depth)
    print(xpos*depth)
}