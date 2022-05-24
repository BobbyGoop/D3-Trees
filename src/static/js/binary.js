class Node {
    constructor(value = null, left = null, right = null, x = null, y = null, level = null) {
        this.value = value;
        this.right = right;
        this.left = left;
        this.x = x;
        this.y = y;
    }

    toString() {
        return JSON.stringify(this);
    }
}

var windowSizes = [240, 480, 960, 1920]

var width = 1000, possibleNodes, height = 1000
var svg = d3.select("svg")
    .attr('height', height)
    .attr('width', width)
var links = svg.append('g').attr('type', 'links')
var circles = svg.append('g').attr('type', 'nodes')


class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    // Симметричный обход
    printInOrder(process) {
        let inOrder = (node) => {
            if (node.left !== null) {
                inOrder(node.left);
            }

            // Коллбек
            process.call(this, node);

            if (node.right !== null) {
                inOrder(node.right);
            }
        };

        inOrder(this.root);
    }

    // Обратный обход
    printPreOrder(process) {
        let preOrder = (node) => {
            process.call(this, node);

            if (node.left !== null) {
                preOrder(node.left);
            }

            if (node.right !== null) {
                preOrder(node.right);
            }
        };

        preOrder(this.root);
    }

    // Прямой обход
    printPostOrder(process) {
        let postOrder = (node) => {
            if (node.left !== null) {
                postOrder(node.left);
            }

            if (node.right !== null) {
                postOrder(node.right);
            }

            process.call(this, node);
        }

        postOrder(this.root);
    }

    traverseBFS() {
        let result = []
        let queue = [this.root];
        while (queue.length > 0) {

            let node = queue.shift();

            result.push(node.value);

            if (node.left) {
                queue.push(node.left);
            }

            if (node.right) {
                queue.push(node.right);
            }
        }
        return result;
    }

    traverseZigZag() {
        let stack = [this.root];
        // store next level node in nextLevel because order changes
        let nextLevel = [];
        let fromLeft = true;
        let result = [];

        while (stack.length) {
            let len = stack.length;

            for (let i = 0; i < len; i++) {
                let el = stack.pop();
                result.push(el.value);
                if (fromLeft) {
                    el.left && nextLevel.push(el.left);
                    el.right && nextLevel.push(el.right);
                } else {
                    el.right && nextLevel.push(el.right);
                    el.left && nextLevel.push(el.left);
                }
            }
            fromLeft = !fromLeft;
            stack = nextLevel;
            nextLevel = [];
        }
        return result;
    }

    // Ищет ноду, возвращает ноду
    find(value) {
        var node = this.root;
        var traverse = function (node) {
            if (!node) return false;
            if (value === node.value) {
                return true;
            } else if (value > node.value) {
                return traverse(node.right);
            } else if (value < node.value) {
                return traverse(node.left);
            }
        };
        return traverse(node);
    }


    // Минимальное значение
    getMin(node = this.root) {
        while (node.left) {
            node = node.left;
        }
        return node;
    }

    // Максимальное значение
    getMax(node = this.root) {
        while (node.right) {
            node = node.right;
        }
        return node.value;
    }

    remove(value, current = this.root) {
        if (current === null) return current
        if (value === current.value) {
            // Если у ноды 1 дочерняя нода или нет вовсе
            if (current.left === null && current.right === null) {
                return null
            } else if (current.left === null) {
                return current.right
            } else if (current.right === null) {
                return current.left
            } else {
                // Если у ноды 2 дочерних ноды, надо 
                // найти "inorder successor", наименьшую ноду 
                // от правого поддерева
                let tempNode = this.getMin(current.right)
                // записываем значение
                current.value = tempNode.value
                /// Удаляем
                current.right = this.remove(tempNode.value, current.right,)
                return current
            }
            // recur down the tree
        } else if (value < current.value) {
            current.left = this.remove(value, current.left,)
            return current
        } else {

            current.right = this.remove(value, current.right,)
            return current
        }
    }

    leastCommonAncestor(n1, n2) {
        if (this.root == null) {
            return this.root;
        }

        let queue = [this.root];
        while (queue.length) {
            let root = queue.shift();
            if (root.value === n1.value ||
                root.value === n2.value ||
                (root.value >= n1.value && root.value <= n2.value) ||
                (root.value <= n1.value && root.value >= n2.value)
            ) {
                return root;
            } else {
                if (root.value > n1.value && root.value > n2.value) {
                    root.left && queue.push(root.left);
                } else {
                    root.right && queue.push(root.right);
                }
            }
        }
        return null;
    }

    findHeight(root = this.root) {
        let height = (node) => {
            if (node === null) {
                return -1;
            }

            let lefth = height(node.left);
            let righth = height(node.right);

            return 1 + Math.max(lefth, righth);
        }
        return height(root);
    }

    isBalanced() {
        let balanced = function (node) {
            if (node === null) { // Base case
                return true;
            }
            let heightDifference = Math.abs(this.findHeight(node.left) - this.findHeight(node.right));
            if (heightDifference > 1) {
                return false;
            } else {
                return balanced(node.left) && balanced(node.right);
            }
        }
        return balanced(this.root);
    }

    contains(value) {
        console.log(this.find(value))
        if (this.find(value) == undefined) return false;
        else return true;
    }

    size() {
        let length = 0;
        this.printInOrder(() => {
            length++;
        });
        return length;
    }

    // Returns an array containing the tree's nodes, in ascending order.
    toArray() {
        let arr = [];
        this.printInOrder((node) => {

            arr.push(node);
            //arr.push(node.value);
        });
        return arr;
    }

    //Returns the tree in order as a serialized JSON string.
    toString() {
        let str = '';
        this.printInOrder((node) => {
            str += JSON.stringify(node.value) + '\n';
        });
        return str;
    }

    //Returns the node with the nth-largest value in the tree.    
    nthLargest(n) {
        let arr = this.toArray();
        return arr[arr.length - (n + 1)];
    }

    // Returns the node with the nth-smallest value in the tree.
    nthSmallest(n) {
        let arr = this.toArray();
        return arr[n];
    }


    insert(value) {
        var deltaX = width / 4;
        var deltaY = 50;
        //var deltaY = deltaX;
        var coordY = 100;
        var coordX = width / 2;
        var level = 0;
        if (this.root === null) {
            this.root = new Node(value, null, null, coordX, coordY);
        } else {
            let current = this.root;
            // While true чтобы в конце все равно создать
            // новую ноду
            while (true) {
                deltaX /= 2;
                //deltaY = deltaX;
                console.log(coordX)
                level++;
                if (value > current.value) {
                    if (current.right === null) {
                        coordY += deltaY;
                        coordX += deltaX;
                        current.right = new Node(value, null, null, coordX, coordY);
                        break;
                    } else {
                        coordY += deltaY;
                        coordX += deltaX;
                        current = current.right;
                    }
                } else if (value < current.value) {
                    if (current.left === null) {
                        coordY += deltaY;
                        coordX -= deltaX;
                        current.left = new Node(value, null, null, coordX, coordY);
                        break;
                    } else {
                        coordY += deltaY;
                        coordX -= deltaX;
                        current = current.left;
                    }
                }
            }
            console.log("Уровень: ", level,
                "  X:", coordX, " Y:", coordY);
        }
    }

    drawCircles() {

        var nodes = this.toArray();
        nodes.forEach((el) => {
            var node = circles.append('g');
            node.append('circle')
                .attr('cx', el.x)
                .attr('cy', el.y)
                .attr('r', 10)
            node.append('text')
                .attr('fill', 'black')
                .attr('x', el.x)
                .attr('y', el.y)
                .attr('text-anchor', 'middle')
                .attr('alignment-baseline', 'middle')
                .attr('font-size', 8)
                .text(el.value)


        });
    }

    drawLinks() {
        var nodes = this.toArray();
        nodes.forEach((node) => {

            var sourceX, sourceY;
            var targetX, targetY;
            if (node.right != null) {
                sourceX = node.x;
                sourceY = node.y;
                targetX = node.right.x;
                targetY = node.right.y;
                links.append('line')
                    .attr('src', node.value)
                    .attr('tgt', node.right.value)
                    .attr('x1', sourceX)
                    .attr('x2', targetX)
                    .attr('y1', sourceY)
                    .attr('y2', targetY);
            }
            if (node.left != null) {
                sourceX = node.x;
                sourceY = node.y;
                targetX = node.left.x;
                targetY = node.left.y;
                links.append('line')
                    .attr('src', node.value)
                    .attr('tgt', node.left.value)
                    .attr('x1', sourceX)
                    .attr('x2', targetX)
                    .attr('y1', sourceY)
                    .attr('y2', targetY);

            }
        })

    }
}

function randomArray(count, min, max) {
    if (count > (max - min)) return;
    var arr = [], t;

    while (count) {
        t = Math.floor(Math.random() * (max - min) + min);
        if (arr.indexOf(t) === -1) {
            arr.push(t);
            count--;
        }
    }

    return arr;
}

var array = randomArray(15, 0, 50)

var ideal = [40, 50, 30, 20, 36, 16, 25, 34, 38, 60, 46, 64, 56, 48, 43,
    14, 17, 23, 26, 32, 35, 37, 39, 42, 44, 47, 49, 54, 58, 62, 66]

var tree = new BinarySearchTree();
array.forEach(el => tree.insert(el))
tree.drawCircles();
tree.drawLinks();

console.log('Высота:', tree.findHeight())
console.log(" Обход дерева зиг-загом", tree.traverseZigZag());
console.log(" Обход дерева по уровням", tree.traverseBFS());
console.log(" Прямой обход: ", tree.printPreOrder((key) => console.log(key.value)));
console.log(" Центрированный обход: ", tree.printInOrder((key) => console.log(key.value)));
console.log(" Обратный обход: ", tree.printPostOrder((key) => console.log(key.value)));
