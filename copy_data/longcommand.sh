am broadcast -a clipper.set -e text "1.new Object跟new Object[0]作为同步锁的引用并没有区别,都可以作为对象同步锁使用；2.new Object[0]创建的是一个对象数组，也有object对象，数组本身就是对象，也会开辟空间存储；new Object会创建一个对象,内存中中会给他开辟一个空间存储他。综上区别不大4.零长度的byte数组对象创建起来将比任何对象都经济,查看编译后的字节码：生成零长度的byte[]对象只需3条操作码,而Object lock = new Object()则需要7行操作码综上new Object跟new Object[0]锁比起来没什么区别，最经济的方式是零长度的byte数组著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"

sleep 0.2
input tap 396 538
exit
