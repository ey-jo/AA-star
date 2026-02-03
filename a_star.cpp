typedef struct node
{
    node *previous;
    int cost;
    int heuristic; 
} Node;

Node* a_star() {
    // calculate distance in some way from current node to goal for A*
}