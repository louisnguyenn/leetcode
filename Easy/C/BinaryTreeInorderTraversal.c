/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int numNodes(struct TreeNode* root)
{
    int left, right;
    int totalNodes= 0;

    if (root == NULL)   // base case
    {
        return 0;
    }

    // recursively count the nodes in the left and right subtrees
    left = numNodes(root->left);
    right = numNodes(root->right);

    totalNodes = left + right + 1;  // add 1 for the root node

    return totalNodes;
}

void BSTPrintInOrder(struct TreeNode* node, int *arr, int *index) {
    int i = 0;

    if (node == NULL) // base case
    {
        return;
    }

    BSTPrintInOrder(node->left, arr, index);
    arr[*index] = node->val;    // add value to array
    (*index)++; // increment the index
    BSTPrintInOrder(node->right, arr, index);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr = NULL;
    int index = 0;

    *returnSize = numNodes(root);

    // allocate memory with the number of nodes in the tree
    arr = malloc(sizeof(int)*(*returnSize));

    /* we initalize index as an integer and pass the memory address to keep
    track of the index of the array to prevent overwriting */
    BSTPrintInOrder(root, arr, &index);

    return arr; // return array;
}
