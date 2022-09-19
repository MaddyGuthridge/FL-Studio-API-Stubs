
Under normal circumstances

* getUndoHistoryLast() returns the index within the visible undo history (0 for most recent)

* getUndoHistoryPos() and getUndoHistoryCount() both return the length of the visible undo history

using setUndoHistoryPos() and setUndoHistoryCount() make this behavior much more confusing.

* Calling setUndoHistoryPos() trims the undo history removing the most recent items. This change in length is reflected by getUndoHistoryPos(), but not by getUndoHistoryCount(), meaning that getUndoHistoryCount() will return a value that doesn't align with what the user can see.

* Contrastingly, calling setUndoHistoryCount() trims the undo history removing the oldest items. This change in length is reflected by getUndoHistoryCount(), but not by getUndoHistoryPos().

Overall, the two dot points above mean that a script can't know how many elements are in the undo history until it checks for the minimum of the two values.

If you're not at the most recent position in the undo history, then the behavior becomes even more confusing.

* Calling setUndoHistoryPos() keeps getUndoHistoryLast() as the same value, rather than reducing it so that it stays pointed to the same element in the history. However, it does not actually undo items to make the location it points to match the actual location in the undo history. When this happens, calling undoDown() will undo those later items in the undo history rather than redoing them (not that there is anything to redo, since they never got undone in the first place).

* Calling setUndoHistoryCount() also keeps getUndoHistoryLast() as the same value, but this doesn't appear to cause any major issues.
