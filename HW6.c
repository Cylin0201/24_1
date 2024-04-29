push(Stack* stack, int data) {
    mutex_lock(stack->lock); // Acquire the lock
    Node* newNode = createNode(data);
    newNode->next = stack->top;
    stack->top = newNode;
    pthread_mutex_unlock(&(stack->lock)); // Release the lock
}

pop(Stack* stack) {
    mutex_lock(stack->lock); // Acquire the lock
    if (stack->top == NULL) {
        printf("Stack is empty\n");
        pthread_mutex_unlock(&(stack->lock)); // Release the lock before exiting
        exit(1);
    }
    Node* temp = stack->top;
    int data = temp->data;
    stack->top = stack->top->next;
    free(temp);
    pthread_mutex_unlock(&(stack->lock)); // Release the lock
    return data;
}