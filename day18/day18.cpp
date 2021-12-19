#include <bits/stdc++.h>
using namespace std;

struct node
{
    int depth;
    int val;
    node *left, *right, *parent;
    int child_dir; // -1 root, 0 left,1 right
    node()
    {
        val = -1;
        depth = 0;
        left = NULL;
        right = NULL;
        parent = NULL;
        child_dir = -1;
    }
    node(int _depth, node *_parent, int _child_dir)
    {
        val = -1;
        depth = _depth;
        parent = _parent;
        left = NULL;
        right = NULL;
        child_dir = _child_dir;
    }
};

void printTree(node *node)
{
    if (node->val != -1)
    {
        cout << node->val << " at depth: " << node->depth << "\n";
        return;
    }
    if (node->left)
    {
        printTree(node->left);
    }
    if (node->right)
    {
        printTree(node->right);
    }
}

void addDepth(node *node, int val)
{
    node->depth++;
    if (node->left)
    {
        addDepth(node->left, val);
    }
    if (node->right)
    {
        addDepth(node->right, val);
    }
}

// returns false if there is node with depth >= 4 or val >= 10
bool check(node *node)
{
    if ((node->val == -1 && node->depth >= 4) || node->val >= 10)
    {
        return false;
    }
    bool ok = true;
    if (node->left)
    {
        ok &= check(node->left);
    }
    if (node->right)
    {
        ok &= check(node->right);
    }
    return ok;
}

// returns the pointer for leftmost valued child of given node
node *findLeftmostChild(node *nownode)
{
    assert(nownode != NULL);
    node *res = NULL;
    if (nownode->left)
    {
        res = findLeftmostChild(nownode->left);
    }
    if (res != NULL)
    {
        return res;
    }
    if (nownode->val != -1)
    {
        return nownode;
    }
    return res;
}

// returns the pointer for rightmost valued child of given node
node *findRightmostChild(node *nownode)
{
    assert(nownode != NULL);
    node *res = NULL;
    if (nownode->right)
    {
        res = findRightmostChild(nownode->right);
    }
    if (res != NULL)
    {
        return res;
    }
    if (nownode->val != -1)
    {
        return nownode;
    }
    return res;
}

void relaxDepth(node *nownode)
{
    assert(nownode != NULL);
    // find just before left val
    node *itr = nownode;
    node *res1 = NULL;
    node *res2 = NULL;
    while (true)
    {
        if (itr->child_dir == 1 && itr->val == -1)
        {
            // find rightmost non -1 value node of node's left child
            res1 = findRightmostChild(itr->parent->left);
            assert(res1 != NULL);
            break;
        }
        if (itr->parent)
        {
            itr = itr->parent;
        }
        else
        {
            break;
        }
    }
    itr = nownode;
    // find just after right val
    while (true)
    {
        if (itr->child_dir == 0 && itr->val == -1)
        {
            // find leftmost non -1 value node of node's left child
            res2 = findLeftmostChild(itr->parent->right);
            assert(res2 != NULL);
            break;
        }
        if (itr->parent)
        {
            itr = itr->parent;
        }
        else
        {
            break;
        }
    }
    if (res1)
    {
        res1->val += nownode->left->val;
    }
    if (res2)
    {
        res2->val += nownode->right->val;
    }
    nownode->val = 0;
    nownode->left = NULL;
    nownode->right = NULL;
}

void relaxValue(node *nownode)
{
    assert(nownode != NULL);
    int lval = nownode->val / 2;
    int rval = (nownode->val + 1) / 2;
    nownode->val = -1;
    nownode->left = new node(nownode->depth + 1, nownode, 0);
    nownode->left->val = lval;
    nownode->right = new node(nownode->depth + 1, nownode, 1);
    nownode->right->val = rval;
    if (nownode->depth >= 4)
    {
        relaxDepth(nownode);
    }
}

node *findDepthNode(node *nownode)
{
    assert(nownode != NULL);
    node *res = NULL;
    if (nownode->left)
    {
        res = findDepthNode(nownode->left);
    }
    if (res != NULL)
    {
        return res;
    }
    if (nownode->depth >= 4 && nownode->val == -1 && nownode->left->val != -1 && nownode->right->val != -1)
    {
        return nownode;
    }
    if (nownode->right)
    {
        res = findDepthNode(nownode->right);
    }
    return res;
}

node *findValueNode(node *nownode)
{
    assert(nownode != NULL);
    node *res = NULL;
    if (nownode->left)
    {
        res = findValueNode(nownode->left);
    }
    if (res != NULL)
    {
        return res;
    }
    if (nownode->right)
    {
        res = findValueNode(nownode->right);
    }
    if (res != NULL)
    {
        return res;
    }
    if (nownode->val >= 10)
    {
        return nownode;
    }
    return NULL;
}

void relax(node *nownode)
{
    // first check for depth 4
    node *depnode = findDepthNode(nownode);
    if (depnode)
    {
        relaxDepth(depnode);
        return;
    }
    // check for val 10
    node *valnode = findValueNode(nownode);
    if (valnode)
        relaxValue(valnode);
}

void relaxHelper(node *nownode)
{
    while (true)
    {
        bool ok = check(nownode);
        if (ok == true)
        {
            break;
        }
        relax(nownode);
        // printTree(nownode);
        // cout << "done in func\n";
    }
    assert(check(nownode) == true);
}

int calculate(node *nownode)
{
    int res = 0;
    if (nownode->left)
    {
        res += 3 * calculate(nownode->left);
    }
    if (nownode->right)
    {
        res += 2 * calculate(nownode->right);
    }
    if (nownode->val != -1)
    {
        return nownode->val;
    }
    return res;
}

node *snailNumbersAddition(node *root, string s)
{
    node *nowroot = new node();
    node *nownode = nowroot;
    for (auto c : s)
    {
        if (c == '[')
        {
            // go one level down to the left child
            node *leftchild = new node(nownode->depth + 1, nownode, 0);
            nownode->left = leftchild;
            nownode = leftchild;
        }
        else if (c == ',')
        {
            // go to the right child of node's parent
            nownode = nownode->parent;
            node *rightchild = new node(nownode->depth + 1, nownode, 1);
            nownode->right = rightchild;
            nownode = rightchild;
        }
        else if (c == ']')
        {
            // go to parent
            nownode = nownode->parent;
        }
        else
        {
            int no = c - '0';
            nownode->val = no;
        }
    }
    if (root == NULL)
    {
        root = nowroot;
        relaxHelper(root);
        return root;
    }
    addDepth(root, 1);
    addDepth(nowroot, 1);
    node *newroot = new node();
    root->child_dir = 0;
    root->parent = newroot;
    nowroot->parent = newroot;
    nowroot->child_dir = 1;
    newroot->left = root;
    newroot->right = nowroot;
    root = newroot;
    relaxHelper(root);
    return root;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    bool first = true;
    vector<string> inp;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        inp.push_back(s);
    }
    {
        // first part
        node *root = NULL;
        for (int i = 0; i < n; i++)
        {
            root = snailNumbersAddition(root, inp[i]);
        }
        cout << calculate(root) << "\n";
    }
    {
        // 2nd part
        int maxi = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if(i == j)continue;
                node *root = NULL;
                root = snailNumbersAddition(root, inp[i]);
                root = snailNumbersAddition(root, inp[j]);
                int tans = calculate(root);
                maxi = max(maxi,tans);
            }
        }
        cout << maxi << "\n";
    }
    return 0;
}