#include "lists.h"

/**
 * insert_node - insert a node at the end of a list
 * @head: head of the list
 * @number: number to insert
 *
 * Return: linked list with the new node
 */
* /
    listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *temp;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }
    temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = new_node;
    return (new_node);
}